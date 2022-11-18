# Nov 2022 Update: PiCamera expired

The NDVI tutorial at https://projects.raspberrypi.org/en/projects/astropi-ndvi is great but I could not get CV2 to work on the supplied AstroPi kit.
It throws up an error about rebuilding a library. 

*A regular install of a Raspberry Pi image from https://www.raspberrypi.com/software/ fixes the error*. The NDVI tutorial now works great.
That is except for the extra bit at the end that talks about using PiCamera. I did try "Re-enabling the Legacy Camera" but Picamera still wasn't working. That's why my files above use PiCamera2.

## Picamera is dead. All hail Picamera2

The later parts of the tutorial that uses the old PiCamera python module no longer works. PiCamera has since been replaced by libcamera on all newer Raspberry Pis. The new python module of libcamera is called picamera2 and as of today is still in beta. Docs and example available at https://github.com/raspberrypi/picamera2

