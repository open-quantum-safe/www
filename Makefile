all:
	git submodule update
	bundle exec jekyll build
	#bash deploy_benchmarking.sh

