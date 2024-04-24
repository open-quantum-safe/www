## Hosting a local copy of this website

### Setup

```bash
gem install bundler
git clone --recursive git@github.com:open-quantum-safe/www
cd www
bundle install
```

### Building the website

You can build a copy of the website into the `_site` directory by running

```bash
bundle exec jekyll build
```

Alternatively, you can have Jekyll launch a process which will (a) serve the website on a local port, and (b) rebuild whenever a file on disk changes:

```bash
bundle exec jekyll serve
```

The output will show the local address that the web server is running on.

Note that `jekyll serve` doesn't seem to pick up some changes, such as changes to the `_config.yml` site configuration file, or if you have a custom plugin (which we don't).

## Updating the liboqs submodule

```bash
git submodule foreach git pull origin main
git add _includes/liboqs
git commit
```

## Rebuilding API documentation

```bash
make doxyjinj
```

Then clean up the diffs so that they have the YML header and don't have their own HTML header / footer.
