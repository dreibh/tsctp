# Test with: sudo make srpm outdir=/tmp

srpm:
	echo "====== Preparing SRPM ======"
	dnf install -y rpmdevtools
	ci/get-dependencies fedora --install
	./make-srpm
	cp $(HOME)/rpmbuild/SRPMS/*.src.rpm $(outdir)
	echo "====== SRPM ready ======"
	ls -l $(outdir)
