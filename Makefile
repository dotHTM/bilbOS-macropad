
currentCPRelease ?= 20250625

DEVICE ?= /Volumes/CIRCUITPY
VENV ?= .venv

default: install

PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
CIRCUP := $(VENV)/bin/circup

$(VENV)/bin/activate:
	virtualenv $(VENV)
	$(PIP) install --upgrade pip

source := https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download
archive := adafruit-circuitpython-bundle-py-${currentCPRelease}.zip
downloadDir := downloads
downloadPath := ${downloadDir}/${archive}
libDir := lib

downloadURL := ${source}/${currentCPRelease}/${archive}

dotZip := .zip
emptystr :=

unarchivedDir = $(subst ${dotZip},${emptystr},${downloadPath})

clean:
	-rm -rf "${libDir}"
	-rm -rf "${downloadDir}"
	-rm -rf "${VENV}"

${downloadPath}:
	mkdir -p "${downloadDir}"
	curl -L "${downloadURL}" -o "${downloadPath}"

download: ${downloadPath}

install: ${downloadPath} requirements-dev.txt $(VENV)/bin/activate
	-rm -rf "${libDir}"
	unzip -o "${downloadPath}" -d "${downloadDir}"
	mv "${unarchivedDir}"/lib "${libDir}"
	"$(PIP)" install -r requirements-dev.txt

sweep:
	find . -iname "._*" -delete
	find . -iname ".DS" -delete

device_clean:
	rm -rf "${DEVICE}"/lib

xfer: sweep
	rsync -hav --delete app/ "${DEVICE}" \
		--exclude .Trashes \
		--exclude .fseventsd \
		--exclude .DS_Store \
		--exclude .Spotlight-V100 \
		--exclude boot_out.txt \
		--exclude lib
	"${CIRCUP}" install -r requirements.txt
	"${CIRCUP}" install -a

eject:
	diskutil eject "${DEVICE}"
