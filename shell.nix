let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in

pkgs.mkShellNoCC {
  packages = with pkgs; [
    (python3.withPackages (ps: with ps; [
      numpy
      scipy
      matplotlib
      sympy
      pip
      pandas
      networkx
    ]))
  ];
}
