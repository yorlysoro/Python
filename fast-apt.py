from  apt.package import Package, Version
from apt import Cache
import apt_pkg
import sys
apt_pkg.init()
entrada = input('-> ')
cache = Cache()
pkg = cache[entrada]
pkgiter = apt_pkg.Cache()[entrada]
program = Package(pkg , pkgiter)
if program.is_installed:
	print(entrada + ' is installed')
else:
	print(entrada + ' is not instaled')
	program.mark_install
	#print("is marked installed ", program.marked_install)
	version = Version(program.shortname, pkg.candidate)
	print(version.version)
		
cache.commit()

#~ import apt
#~ import sys

#~ from apt.progress import InstallProgress

#~ class TextInstallProgress(InstallProgress):
	#~ def __init__(self):
		#~ apt.progress.InstallProgress.__init__(self)
		#~ self.last = 0.0
		
	#~ def updateInterface(self):
		#~ InstallProgress.updateInterface(self)
		#~ if self.last >= self.percent:
			#~ return
		#~ sys.stdout.write("")


#~ pkg = apt.Cache()

#~ pkg.update()
#~ for updates in pkg:
	#~ if updates.is_upgradable:
		#~ print(updates.candidate.uri)

#~ pkg.mark_install
