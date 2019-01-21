srpm:
	cd .. && \
	ci/get-dependencies fedora --install && \
	./make-srpm && \
	cp $(HOME)/rpmbuild/SRPMS/*.src.rpm $(outdir)
