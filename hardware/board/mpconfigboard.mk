LD_FILE = boards/samd21x18-bootloader-external-flash-crystalless.ld
#LD_FILE = boards/samd21x18-bootloader.ld
USB_VID = 0x239A
USB_PID = 0x801F
USB_PRODUCT = "cpBadge1411"
USB_MANUFACTURER = "Radomir Dopieralski"

SPI_FLASH_FILESYSTEM = 1

CHIP_VARIANT = SAMD21E18A
CHIP_FAMILY = samd21

LONGINT_IMPL = MPZ

FROZEN_MPY_DIRS += $(TOP)/frozen/cpbadge1411
