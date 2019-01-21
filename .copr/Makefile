# Test with: sudo make srpm outdir=/tmp

srpm:
	echo "====== Preparing SRPM ======"
	ls -l
	pwd
	ci/get-dependencies fedora --install && ./make-srpm && cp $(HOME)/rpmbuild/SRPMS/*.src.rpm $(outdir)
	echo "====== SRPM ready ======"
	ls -l $(outdir)
