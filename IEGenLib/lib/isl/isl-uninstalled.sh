# generated by configure / remove this line to disable regeneration
prefix="/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/installed"
exec_prefix="${prefix}"
bindir="${exec_prefix}/bin"
libdir="/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/isl/.libs"
datarootdir="${prefix}/share"
datadir="${datarootdir}"
sysconfdir="${prefix}/etc"
includedir="/home/KALYANBHETWAL/HyPe-DSL/IEGenLib/lib/isl/./include"
package="isl"
suffix=""

for option; do case "$option" in --list-all|--name) echo  "isl"
;; --help) pkg-config --help ; echo Buildscript Of "isl Library"
;; --modversion|--version) echo "0.16.1"
;; --requires) echo : ""
;; --libs) echo -L${libdir} "" "-lisl"
       :
;; --cflags) echo -I${includedir} "-std=gnu99 -I./imath_wrap"
       :
;; --variable=*) eval echo '$'`echo $option | sed -e 's/.*=//'`
;; --uninstalled) exit 0 
;; *) ;; esac done