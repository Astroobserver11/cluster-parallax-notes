# High-Cadence Optical Pulsar Photometry Experiment
Date: 2026-10-25

## Concept
Test the plasma-universe proposition that pulsars are relaxation circuits rather than gravitationally modulated rotators. The discriminating observable: if optical pulsations show harmonics of the radio spin frequency (2f, 3f) with no fundamental, or optical-radio phase relationships inconsistent with a rotating beam, that supports a circuit/relaxation model over a lighthouse model. A shared fundamental period alone cannot discriminate — any rotating beam produces the same clock in every band.

## Instrument Configuration
- Aperture: minimum 10 inches (25 cm), larger preferred for photon statistics on faint targets
- Detector: Sony CMOS chip at 178 frames per second
- Nyquist frequency: 89 Hz
- Implication: pulsar spin frequencies must be below 89 Hz (periods above ~11.2 ms) for direct sampling without aliasing
- Long evenly-gated series can in principle recover super-Nyquist frequencies via aliases, but the alias forest for sharp pulses is dense and symmetric; pulse profile shape (width, asymmetry) is needed to break degeneracies between true frequency and mirrors
- TESS sector gaps punch holes in the window function and smear alias peaks — not a factor for ground-based continuous runs
- Differential photometry: ratio target against several non-variable field stars in the same frame to cancel common-mode scintillation and transparency variations
- Narrow-band filter around the pulsar's emission wavelength improves contrast
- No adaptive optics required: seeing is broadband red-noise turbulence (smooth spectral slope), while a coherent pulsation appears as a narrow spike whose SNR grows with square root of integration time. Fourier transform separates them cleanly. Radio ephemerides provide the candidate frequency, converting a blind search into a single-hypothesis test.

## Target List: Optically Detected Pulsars (13 recognized as of 2018)
Sorted by B magnitude. Period converted to spin frequency for Nyquist check (89 Hz limit).

| Pulsar | B mag | Period (ms) | Spin freq (Hz) | Nyquist status | Notes |
|---|---|---|---|---|---|
| Crab (PSR B0531+21) | 16.5 | 33 | 30.2 | ACCESSIBLE | Brightest by far; 3,300 B photons per rotation on VLT; optical-radio lag 321 us measured; double-peaked; 9.7% polarization |
| PSR J0437-4715 | 20.98 | 5.76 | 174 | OUT OF REACH | Fastest MSP; above Nyquist at 178 fps; would need 350+ fps |
| PSR J1023+0038 | 22 | transitional MSP | variable | MARGINAL | Transitional; optical pulsations detected in some states; companion heating dominates light curve |
| PSR B0540-69 (LMC) | 23 | 50 | 20.0 | ACCESSIBLE | 49 kpc — flux diluted; 17 B photons/rotation on VLT |
| Vela (PSR B0833-45) | 24 | 89 | 11.2 | ACCESSIBLE | 230 pc — nearest; 12 B photons/rotation on VLT; 8.1% polarization |
| PSR B1055-52 | 24.9 | 197 | 5.1 | ACCESSIBLE | UV/optical detection; no confirmed pulsations in some bands |
| PSR B0656+14 | 25-26 | 385 | 2.6 | ACCESSIBLE | 290 pc; 100% polarization measured; 13 B photons/rotation on VLT |
| Geminga (PSR B0633+17) | 25.5 | 237 | 4.2 | ACCESSIBLE | 160 pc; 25.5 B photons/rotation on VLT; multicomponent SED |
| PSR B1509-58 | 25.7 | 151 | 6.6 | ACCESSIBLE | Polarization ~10.4%; R=25.7 |
| PSR B1929+10 | 25.6 | 227 | 4.4 | ACCESSIBLE | UV detection only in some bands |
| PSR J0108-1431 | 26.4 | ~ | ~ | ACCESSIBLE | Very faint |
| PSR B0950+08 | 27.1 | 253 | 4.0 | ACCESSIBLE | UV/optical |
| PSR B1133+16 | 28 | ~1190 | 0.84 | ACCESSIBLE | Extremely faint for 10-inch |

## The Match
Frequency accessibility is nearly universal — only J0437-4715 (174 Hz) exceeds the 89 Hz Nyquist. The real filter is brightness. Crab at B=16.5 is the only target comfortably within reach of a 10-inch aperture at 178 fps. Vela (24) and B0540-69 (23) are marginal — detectable in principle with heavy stacking and excellent sites, but photon-starved. Everything fainter than ~24 requires apertures well beyond 10 inches or impractically long integrations.

**Primary target: Crab.** Secondary: Vela. Tertiary: B0540-69 if LMC access and site quality permit.

## AAVSO Angle
Lead with time-domain photometry of a known variable, not pulsar-circuit theory. AAVSO has run high-cadence campaigns; a 178-fps CMOS dataset on Crab would be novel for their archive. Frame the proposal as optical monitoring with fast photometry — the harmonic-discrimination analysis is the downstream scientific product.

## Falsifiability
- Optical power at 2f or 3f with no fundamental → supports relaxation-circuit model
- Optical-radio phase lag inconsistent with magnetospheric beam geometry → supports non-rotational modulation
- Clean fundamental at f with phase lag matching known magnetospheric models → consistent with standard rotation model (null result for the plasma proposition, but still a valid dataset)
- No detectable optical pulsation above seeing noise floor → instrument or target too faint; not a model test

## Open Questions
- Can 10-inch + 178 fps reach Vela's 12 B photons/rotation with sufficient stacking? Estimate: need ~10^4-10^5 rotations for 5-sigma on a 10% pulsed fraction — hours to days of continuous dark time.
- Does Crab's known 321-us optical-radio lag vary with time in a way that constrains emission-region geometry?
- Are there unconfirmed optical counterparts among bright radio pulsars (P > 11 ms, B < 22) not yet in the 13-source list?
- SiFAP2 at TNG has done MSP optical searches with null results — what pulsed-magnitude upper limits transfer to a 10-inch CMOS setup?
