export RUSTUP_TOOLCHAIN=nightly
export RUSTUP_HOME=$(rustup show home)
export RUSTC=$(command -v rustc)
export CARGO=$(command -v cargo)
export CARGO_HOME=$HOME/.cargo
export RUSTC_WRAPPER=/home/osolarin/ReproducibleTests/RustRepro/mean-rustc