# based on Makefile for the OCaml package Streaming

.PHONY: check
check:
	git diff-index --quiet HEAD -- || (echo "There are uncommitted changes."; exit 1)
	if git ls-files . --exclude-standard --others --error-unmatch; then \
		echo "There are untracked files."; \
		exit 1; \
	else \
		echo "Ignore the \"error: pathspec '.'...\""; \
		exit 0; \
	fi

.PHONY: publish
publish: check
	rsync -av --exclude-from='.exclude' . ./.build --delete
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
