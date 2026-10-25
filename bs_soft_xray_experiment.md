# Observational Experiment: Blue Stragglers and Soft X-ray Excess
Date: 2026-10-25

## Hypothesis
Blue stragglers (BSs) in globular clusters produce soft X-ray emission (0.5-2 keV) above what is expected from the field population and from known cataclysmic variables / quiescent LMXBs. The excess correlates with BS specific frequency and cluster encounter rate.

## Target Clusters (eROSITA-detected, BS-rich)
1. 47 Tuc (NGC 104) - highest BS count, 14 eROSITA members already classified
2. Omega Centauri (NGC 5139) - largest BS population, eRASS1 source detected
3. NGC 2808 - 16 brightest eROSITA sources, dense core
4. M4 (NGC 6121) - nearest cluster, eRASS1 detection, low crowding
5. NGC 1851 - eRASS1 bright source, known BS population
6. NGC 6441 - eRASS1 detection, high encounter rate
7. Liller 1 - eRASS1 brightest, extreme density
8. Terzan 2 - eRASS1 detection
9. NGC 4372 - eRASS1 detection, low density comparison

## Data Layers
1. **eROSITA eRASS1/eRASS:5** - soft band (0.5-2 keV) source lists, count rates, hardness ratios
2. **HST UV Legacy Survey** (Piotto et al.) - BS catalogs with photometry for all 9 targets
3. **Gaia DR3** - proper motion membership, parallax distance confirmation
4. **Ground-based CMDs** - optical/IR for BS confirmation and field decontamination

## Analysis Steps
1. Cross-match eROSITA sources with BS positions (search radius ~2-3 arcsec, scaled by crowding)
2. Compute BS surface density per cluster core
3. Stack soft X-ray counts at BS positions vs random field positions (control)
4. Fit residual soft excess after subtracting known CV/qLMXB contributions
5. Correlate residual excess with BS specific frequency (N_BS/N_HB) and Gamma (encounter rate)
6. Check for spatial correlation with BS radial distribution profile

## Controls
- Random positions within same annular bins (same crowding, same background)
- Non-BS main-sequence stars matched in brightness
- Clusters with low BS frequency as negative control (e.g., NGC 4372)

## Success Criteria
- Soft excess at BS positions significant at >3 sigma above controls
- Correlation coefficient r > 0.5 between excess and BS frequency or encounter rate
- Spatial match to BS radial profile better than to other populations

## Instruments for Follow-up
- SPHEREx: IR photometry for BS confirmation, triggered star formation tracers
- eROSITA eRASS:5: deeper soft X-ray stack
- Chandra: arcsecond resolution for individual BS counterparts if eROSITA stack positive
- HST/JWST: UV spectroscopy of candidate BS X-ray counterparts

## Open Questions
- Is the soft excess from BS themselves (magnetic activity, winds) or from binary companions?
- Do BS in low-density clusters (tidal tails) show the same signature?
- Can the excess distinguish BS formation channels (collision vs mass transfer)?
