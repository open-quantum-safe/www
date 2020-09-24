all:
	git submodule update
	bundle exec jekyll build
