# based on Makefile for the OCaml package Streaming

.PHONY: check-uncommitted
check-uncommitted:
	git diff-index --quiet HEAD -- || (echo "There are uncommitted changes."; exit 1)
	if [[ $(git ls-files . --exclude-standard --others) ]]; then \
		echo "There are untracked files."; \
		exit 1; \
	fi

.PHONY: build
build:
	rsync -av --exclude-from='.exclude' . ./.build --delete

.PHONY: publish
publish: build check-uncommitted build
	git checkout main
	rm -r *
	cp -r .build/* .
	if git diff-index --quiet HEAD -- .; then \
		echo "There are no changes to the webpage"; \
	else \
		git add *; \
		git commit -m "update webpage"; \
		git push public main; \
	fi
	git checkout -
