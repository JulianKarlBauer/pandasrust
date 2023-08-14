Trying to follow tutorial
"Developing pandas extensions in Rust"
on EuroScipy2023

# Start developing rust

```bash
cargo new counters
cd counter
cargo run
```

# Recommendations

If you want to work on a bunch of strings, use pyarrow instead of numpy.array.

Within arrow, we don't directly point to data, but to metadata which specifies chunks/locations where data lives.
