


currentCPRelease := 20220127
source := https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download
archive := adafruit-circuitpython-bundle-py-${currentCPRelease}.zip
downloadDir := downloads
downloadPath := ${downloadDir}/${archive}
libDir := lib

dotZip := .zip
emptystr := 

unarchivedDir = $(subst ${dotZip},${emptystr},${downloadPath})

default: install

clean:
	-rm -rf ${libDir}
	-rm -rf ${downloadDir}

${downloadPath}:
	mkdir -p ${downloadDir}
	curl -L "${source}/${currentCPRelease}/${archive}" -o "${downloadPath}"

download: ${downloadPath}

install: ${downloadPath} requirements-dev.txt
	-rm -rf ${libDir}
	unzip -o "${downloadPath}" -d ${downloadDir}
	mv "${unarchivedDir}/lib" ${libDir}
	pip3 install -r requirements-dev.txt
	@echo 
	@echo 
	@echo "Remember to add '${shell pwd}/lib' to PYTHONPATH "
	@echo 

xfer:
	find . -iname "._*" -delete
	find . -iname ".DS" -delete
	rsync -hav --delete app/ /Volumes/CIRCUITPY \
		--exclude .Trashes \
		--exclude .DS_Store \
		--exclude .Spotlight-V100 \
		--exclude boot_out.txt \
		--exclude lib
	circup install -r requirements.txt
	circup install -a
