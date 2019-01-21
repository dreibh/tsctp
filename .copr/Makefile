srpm:
	echo "====== Preparing SRPM ======"
	cd .. && ci/get-dependencies fedora --install && ./make-srpm && cp $(HOME)/rpmbuild/SRPMS/*.src.rpm $(outdir)
	echo "====== SRPM ready ======"
	ls -l $(outdir)
