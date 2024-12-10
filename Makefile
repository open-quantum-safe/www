all:
	git submodule update
	bundle exec jekyll build
	bash deploy_benchmarking.sh

doxyjinj:
	cd _doxygen_pretty && python3 doxyjinj.py struct_file.html ../_includes/liboqs/build/docs/xml/struct_o_q_s___k_e_m.xml 'https://github.com/open-quantum-safe/liboqs/tree/main/' > ../liboqs/api/oqskem.html
	cd _doxygen_pretty && python3 doxyjinj.py struct_file.html ../_includes/liboqs/build/docs/xml/struct_o_q_s___s_i_g.xml 'https://github.com/open-quantum-safe/liboqs/tree/main/' > ../liboqs/api/oqssig.html
	cd _doxygen_pretty && python3 doxyjinj.py header_file.html ../_includes/liboqs/build/docs/xml/common_8h.xml 'https://github.com/open-quantum-safe/liboqs/tree/main/' > ../liboqs/api/common.html
	cd _doxygen_pretty && python3 doxyjinj.py header_file.html ../_includes/liboqs/build/docs/xml/kem_8h.xml 'https://github.com/open-quantum-safe/liboqs/tree/main/' > ../liboqs/api/kem.html
	cd _doxygen_pretty && python3 doxyjinj.py header_file.html ../_includes/liboqs/build/docs/xml/rand_8h.xml 'https://github.com/open-quantum-safe/liboqs/tree/main/' > ../liboqs/api/rand.html
	cd _doxygen_pretty && python3 doxyjinj.py header_file.html ../_includes/liboqs/build/docs/xml/sig_8h.xml 'https://github.com/open-quantum-safe/liboqs/tree/main/' > ../liboqs/api/sig.html
	cd _doxygen_pretty && python3 doxyjinj.py header_file.html ../_includes/liboqs/build/docs/xml/sig_stfl_8h.xml 'https://github.com/open-quantum-safe/liboqs/tree/main/' > ../liboqs/api/sig_stfl.html
