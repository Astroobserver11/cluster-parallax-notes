# Industrial Camera Survey for High-Cadence Pulsar Photometry
Date: 2026-10-25

## Context
Follow-on to pulsar_high_cadence_photometry_experiment.md. The experiment needs a camera that (1) samples at or above 178 fps for an 89 Hz Nyquist, (2) has global shutter to avoid rolling-shutter distortion on a moving telescope, (3) gathers enough photons per frame on a 10-inch aperture for Crab (B=16.5) and marginally for Vela (B=24) and B0540-69 (B=23), and (4) has low read noise so that faint-frame stacking doesn't drown the pulsed signal. This survey covers the industrial machine-vision and high-speed camera market that already solves the frame-rate and global-shutter problems at commodity prices.

## Key Sensor Families

### Sony Pregius / Pregius S (global shutter CMOS)
- The workhorse of industrial high-speed imaging. Backside-illuminated (BSI) Pregius S sensors offer QE potentially above 70% with low read noise.
- IMX273: 1.6 MP, 3.45 um pixels, 250 fps USB 3.0, mono and color. Cheap (~$500). Good entry point.
- IMX392: 2.3 MP, 3.45 um, 160 fps USB 3.0 (Basler ace 2). NIR-sensitive variants available.
- IMX900: 3.2 MP, 2.74 um BSI, 114 fps USB 3.0 mono (Basler ace 2 a2A2048-114umPRO); up to 1164 fps in ROI mode on some platforms (e-con Systems e-CAM56_CUOAGX). NIR sensitivity flagged as a plus for low-light factory work.
- IMX925: 24.5 MP stacked BSI global shutter, 442 fps at 8-bit, 394 fps at 10-bit, 212 fps at 12-bit. Type 1.2, 2.74 um pixels. Announced late 2024, shipping 2025. This is the frame-rate ceiling of current industrial sensors at high resolution.
- IMX926: 12.4 MP, 660 fps at 8-bit, 588 fps at 10-bit. Smaller format.
- IMX927: 105 MP at 100 fps (2025 announcement) — resolution-first, not speed-first.
- Baumer CX series: Sony Pregius/Pregius S and onsemi PYTHON, up to 225 fps full frame, 1000 fps in ROI, exposures from 1 us. Industrial temperature range to 65 C.
- Allied Vision FXO: Pregius S sensors, 30-217 fps on 10GigE, up to 671 fps on 100GigE. RDMA transport for stable high-throughput.

### onsemi PYTHON (global shutter CMOS)
- IDS uEye CP series: PYTHON 500 reaches 560+ fps at 0.5 MP; PYTHON 1300 at 169 fps (1.3 MP); PYTHON 5000 at 68 fps (5 MP). 4.8 um pixels, large and light-sensitive by industrial standards. AOI/ROI readout pushes past 1000 fps.
- CMV series (CMOSIS): CMV12000 delivers 300 fps at 12 MP. Sensitivity 6-8 V/lux.s at 550 nm, dark noise 8-20 e-, dynamic range 60-66 dB.

### Scientific / photon-counting tier (not industrial but relevant ceiling)
- Hamamatsu ORCA-Quest 2: qCMOS, 0.3 e- read noise, 85% peak QE at 460 nm, 120 fps full frame (25 fps ultra-quiet), 4096x2304, 4.6 um. Used on Magellan Clay as proto-Lightspeed for optical pulsar work — sub-electron read noise resolving individual photoelectrons on Crab.
- Andor Marana 4.2BV-11: sCMOS, 95% peak QE at 550-570 nm, 1.57 e- read noise, 11 um pixels, vacuum-cooled to -25 C. Validated for high-precision time-series photometry at NGTS (exoplanet transits) against a CCD reference.
- Axiom Optics CB2: global shutter CMOS up to 1594 fps (7366 fps ROI), 2.74-9 um pixels, 816x624 to 5328x4608.
- Revealer S-Series: 15,000 fps full frame at 1280x1024, 14.6 um pixels, 100 ns minimum exposure, 96-192 GB onboard RAM. Extreme but expensive.
- HiCAM Fluo: intensified CMOS, 10 ns gating, 1000-2000 fps. Single-photon capable.
- SPAD512/SPAD Alpha: gated SPAD arrays, zero read noise, up to 100,000 fps at 1-bit. Photon counting.

### CCD legacy (global shutter by design, slower)
- Basler ace Classic ICX424/ICX618: VGA CCD global shutter, 90-120 fps. Superior uniformity but readout-limited. Mostly superseded by CMOS for speed.
- FLIR/Teledyne Blackfly S: IMX287 at 291 fps (0.4 MP, 6.9 um, 65% QE); IMX545 at 10 fps (12.3 MP).

## What Matters for Pulsar Photometry Specifically

1. **Frame rate vs bit depth tradeoff**: IMX925 does 442 fps only at 8-bit. 12-bit drops to 212 fps. For Crab at 30 Hz you need 60+ fps minimum; 178 fps gives margin. 8-bit is fine for differential photometry if gain is set so the pulsed fraction doesn't saturate.
2. **Pixel size vs aperture**: 2.74-3.45 um pixels on a 10-inch telescope at typical f/ratios oversample the seeing disk. That's fine — you bin in software. Larger pixels (5.86 um IMX174/IMX249 class) collect more photons per pixel but the industrial versions are slower (41 fps for IMX249 on Basler Blackfly).
3. **Read noise**: Industrial sensors run 2-5 e-; scientific sCMOS 1-1.6 e-; qCMOS 0.3 e-. For Crab (3300 B photons/rotation on VLT — on a 10-inch that's maybe 30-50 photons/rotation across the PSF), read noise per frame matters less than total integration because you're stacking thousands of rotations. For Vela (12 photons/rotation on VLT), sub-electron read noise becomes the differentiator.
4. **Global shutter is non-negotiable**: a rolling shutter on a tracking telescope smears the PSF along the scan direction every frame. All recommended sensors above are global shutter.
5. **Duty cycle**: IDS fireball photometry paper used IMX426 (Allied Vision Alvium) at 470-500 fps with 1800-1925 us exposures — 90% duty cycle. That's the template: maximize exposure within the frame period, don't waste time on readout.
6. **Triggering and timestamping**: hardware trigger input and precise frame timestamps are standard on Basler/Allied Vision/Baumer. Essential for folding against radio ephemerides.
7. **C-mount**: all industrial cameras use C-mount, which adapts to telescope focusers with off-the-shelf spacers. No custom machining.

## Recommended Tiers

**Tier 1 — Commodity entry (under $1,000)**: Basler ace 2 or IDS uEye CP with IMX273 (250 fps) or IMX392 (160 fps). Prove the pipeline: differential photometry, Fourier spike detection, ephemeris folding. Crab is the only realistic target.

**Tier 2 — Speed + sensitivity ( $1,500-4,000)**: Basler ace 2 with IMX900 BSI mono (114 fps, NIR-sensitive) or Allied Vision Alvium with IMX426 (470-500 fps demonstrated in fireball photometry). Opens Vela and B0540-69 as marginal targets with heavy stacking.

**Tier 3 — Scientific ceiling ( $10,000-30,000)**: Hamamatsu ORCA-Quest 2 (qCMOS, 0.3 e- noise, 85% QE) or Andor Marana (95% QE, 1.57 e-). This is the class already used for optical pulsar detection on large telescopes. On a 10-inch it still won't reach Geminga, but it maximizes what Crab and Vela can yield and future-proofs for a bigger aperture later.

## The Honest Bottom Line
Industrial cameras solve the sampling and shutter problems cheaply. They do not solve the photon problem — that is set by aperture and target brightness, not by the camera. The survey confirms: buy Tier 1 now, run Crab, and let the data tell you whether Tier 2 or 3 is worth the spend.

## Sources
- Baumer CX series global shutter cameras: https://www.baumer.com/us/en/product-overview/industrial-cameras-image-processing/industrial-cameras/cx-series/vcxg-vcxu-cameras/global-shutter-cameras/c/14192
- Allied Vision FXO 100GigE: https://www.1stvision.com/machine-vision-solutions/2026/07/allied-vision-fxo-cameras-to-100gige-and-671fps.html
- IDS uEye CP PYTHON sensors: https://www.eeworldonline.com/cmos-vision-sensors-handle-1000-framessec/
- e-con Systems e-CAM56_CUOAGX (IMX568 BSI, 1164 fps ROI): https://www.edge-ai-vision.com/2024/05/why-e-con-systems-latest-5mp-global-shutter-camera-is-ideal-for-factory-automation/
- Sony IMX925/926 announcement: https://petapixel.com/2024/11/22/sonys-new-24-5mp-global-shutter-sensor-shoots-at-up-to-442-fps/
- Sony IMX927 (105 MP, 100 fps): https://www.sony-semicon.com/en/info/2025/2025092901.html
- Sony Pregius overview: https://www.sony-semicon.com/en/products/is/industry/global-shutter.html
- CMV12000 sensor specs: https://www.photonics.com/Articles/CMOS-Sensors-Boost-High-End-Industrial-Vision/a56479
- Vision Datum IMX273 250 fps: https://shop.visiondatum.com/products/kr-250fps-imx273-1-6mp-usb3-global-shutter-camera
- Fireball photometry with Allied Vision Alvium IMX426 at 470-500 fps: https://arxiv.org/abs/2602.19447 and https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/photometry-of-fireballs-using-high-frame-rate-cameras/644727B1E2BC5D87B1180A6B3B32C927
- Marana sCMOS photometry validation (NGTS): https://arxiv.org/abs/2510.14484
- ORCA-Quest 2 qCMOS pulsar photometry: https://arxiv.org/html/2610.07137v1
- Axiom Optics high-speed scientific cameras: https://www.axiomoptics.com/products/scientific-industrial-cameras/high-speed/
- Shearer APD photon-counting pulsar camera: https://www.academia.edu/22834668/An_avalanche_photodiode_photon_counting_camera_for_high_resolution_astronomy
- CMOS vs CCD exoplanet photometry (Oxford Instruments): https://www.oxinst.com/learning/view/article/comparative-photometry-with-marana-cmos-and-ikon-l-ccd-cameras-at-the-ngts-facility
- RTN mitigation in fast CMOS photometry: https://arxiv.org/abs/2605.19022
- High-speed multicolor CMOS photometry (Nikon D90 test): https://arxiv.org/abs/1205.5924
- Vadzo global shutter comparison: https://www.vadzoimaging.com/post/top-10-global-shutter-camera-for-robotics-automation
- Basler frame rate calculator: https://codingace.net/general/basler_frame_rate.html
- Basler ace 2 portfolio: https://www.accio.com/business/basler-camera-specifications
- FLIR Blackfly S specs: https://www.star-spectrum.com/product-details/flir/
- Cloudy Nights IMX925 discussion (astro use case): https://www.cloudynights.com/forums/topic/949130-four-newly-announced-sony-sensors-with-crazy-high-frame-rates/
- GXCCD C2 global shutter CMOS astro cameras: https://www.gxccd.com/art?id=579&lang=409
- Atik Sony IMX comparison: https://www.atik-cameras.com/news/sony-imx-cmos-sensors-a-practical-comparison-guide/
- Revealer S-Series: https://www.axiomoptics.com/products/revealer-high-speed-camera-s-series/
- Forza Silicon IISW 2025 low-noise high-frame-rate GS sensor: https://imagesensors.org/papers/10.60928/cfm9-2fol
- Mouser Basler portfolio PDF: https://www.mouser.com/datasheet/2/857/BAS2008_Computer_Vision_Portfolio_Brochure_A4_EN_S-1903376.pdf
- Basler A406k 209 fps Camera Link: https://www.photonicsonline.com/doc/basler-launches-fastest-four-megapixel-0001
- Basler PYTHON cameras: https://www.vision-systems.com/cameras-accessories/article/16740690/industrial-camera-line-from-basler-now-features-python-cmos-image-sensors
- Basler ace Classic CCD/CMOS table: https://www.altavision.com.br/EN/GigE_Basler.html
- Basler EMVA data: https://assets-ctf.baslerweb.com/dg51pdwahxgw/1hcLdj4BXRUzhnOL2gaNIm/faa0fa7fe5ea641aca3c3be7efe82c24/BAS2606_EMVA_Data_Overview_A4_EN_SAP0136_No_18.pdf
- Basler ace 2 9.1MP: https://pondesk.com//product/basler-ace-2-91mp-gige-industrial-camera-global-shutter-smvs-028
- Basler boost 65MP: https://aiscomponents.com/brands/basler
