_theme="cvm-spinner"
pkgname="cvm-plymouth-theme"
pkgver="1"
pkgrel=1
pkgdesc="Cvm UI Desktop plymouth theme"
arch=("any")
depends=("plymouth")

package() {
	cp -r ../cvm-spinner .
    cd cvm-spinner
	cp "../../assets/watermark.png" .
	cp "../../assets/bgrt-fallback.png" .
	install -m755 -d $pkgdir/usr/share/plymouth/themes/cvm-spinner
	install -m644 -t $pkgdir/usr/share/plymouth/themes/cvm-spinner *

	cd ..

	# BGRT
	cp -r "../bgrt-cvm" .
    cd "bgrt-cvm"
	install -m755 -d "${pkgdir}/usr/share/plymouth/themes/bgrt-cvm"
	install -m644 -t "${pkgdir}/usr/share/plymouth/themes/bgrt-cvm" *
}
