# Millenia eV

This program implements controls for the pump laser in the MHz system.

There are commands for reporting and setting both the pump power and shutter state. Both of these commands take an `-s` flag for setting the corresponding value. For instance, setting the pump power looks like this:
```
$ pump power -s 3.5
$ pump power
3.51W
```

## Installation
The binary wheel is built using `poetry` inside the project directory. 
```
$ poetry build
```

This builds a program called `pump`, rather than `millenia_ev`, for the sake of convenience. The binary will be installed in the new `dist` directory.

Install the wheel using `pip`:
```
$ python -m pip install dist/millenia_ev-<some stuff>.whl
```

Now you can call the program from any directory:
```
$ cd ~
$ pump shutter -s close
```

## License

Licensed under either of

 * Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
 * MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally
submitted for inclusion in the work by you, as defined in the Apache-2.0
license, shall be dual licensed as above, without any additional terms or
conditions.