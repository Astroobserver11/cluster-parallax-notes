# Comparative Experiment: Blue Stragglers in Globular vs Open Clusters
Date: 2026-10-25 (updated with TESS asteroseismology diagnostic)

## Motivation
Two competing formation channels: direct stellar collisions (dense cores) and binary mass transfer (loose environments). User hypothesis: proper motion studies show velocity dispersions too low for collision rates to dominate, and mass transfer requires Roche-lobe contact at only a few stellar radii — a much larger cross-section. Yet RV surveys find only 20-40% of BSs are binaries. Chemical signatures (C/O enrichment) support accretion in some cases. This experiment tests whether both channels are weak explanations by comparing BS populations across the density spectrum.

## Cluster Samples

### Globular Clusters (dense, old, metal-poor)
- 47 Tuc (NGC 104): highest BS count, eROSITA members classified
- Omega Centauri (NGC 5139): largest BS population
- NGC 2808: dense core, eRASS1 sources
- M4 (NGC 6121): nearest, low crowding
- NGC 1851, NGC 6441, Liller 1, Terzan 2, NGC 4372
- Density range: 10^3 to 10^6 solar masses per cubic parsec
- Age: 10-13 Gyr
- Metallicity: [Fe/H] -0.5 to -2.3

### Open Clusters (sparse, young, metal-rich)
- NGC 2682 (M67): ~4 Gyr, solar metallicity, well-studied BS population, known binary BSs
- NGC 188: ~7 Gyr, old open cluster, BS population studied
- NGC 6819: ~2.5 Gyr, BS population with Gaia membership; TESS CVZ target
- NGC 7789: ~1.6 Gyr, large BS sample
- Berkeley 39: ~6 Gyr, sparse, low-density comparison
- Trumpler 5: old, sparse
- NGC 6791: ~8 Gyr, TESS CVZ target, sparse enough for clean BS light curves
- Density range: 1 to 10^2 solar masses per cubic parsec
- Age: 0.5 to 8 Gyr
- Metallicity: near solar to slightly subsolar

## Key Diagnostics

### 1. Binary Fraction Among BSs
- Method: multi-epoch RV monitoring (HARPS, UVES, APOGEE) + Gaia astrometric binaries
- GC expectation if mass transfer dominates: high binary fraction (>50%)
- GC expectation if collisions dominate: low binary fraction (<20%)
- OC expectation: high binary fraction regardless of channel (loose environment favors binaries surviving)
- Diagnostic power: if OCs show high BS binary fractions AND GCs show low ones, supports density-dependent channel switching. If both show similar intermediate fractions (~30%), suggests a third channel or observational bias (face-on, long-period systems).

### 2. Rotational Velocities (v sin i)
- Method: high-resolution spectroscopy
- Collision products: spun up, high rotation (tens to hundreds km/s), magnetic braking over Gyr
- Mass-transfer accretors: spun up but tidal braking with evolved donor can slow them
- Diagnostic: if GC BSs are slow rotators despite youth (relative to main sequence), either braking is efficient or they are not collision products. OCs are too young for significant braking, so fast rotators there would support collision channel in at least some cases.

### 3. Chemical Abundance Patterns
- Method: high-res spectroscopy (APOGEE, UVES)
- C/O enrichment: signature of CNO-processed material from evolved donor → mass transfer
- No enrichment or depletion: consistent with collision (mixing of unprocessed envelopes)
- Lithium: preserved in some BSs, depleted in others — age and mixing diagnostic
- Diagnostic: if GC BSs show mixed C/O signatures (some enriched, some not), both channels operate. If OCs show uniform enrichment, mass transfer dominates there.

### 4. Spatial Distribution Relative to Core
- Method: HST/Gaia radial profiles
- Collision channel: BSs concentrated in core (highest encounter rate)
- Mass transfer: BSs follow binary distribution, may be more extended
- Diagnostic: core-concentrated BSs in GCs support collisions; extended BS halos in OCs support binary evolution. Mismatch (e.g., extended BSs in dense GC cores) suggests neither channel dominates.

### 5. BS Specific Frequency vs Cluster Parameters
- Method: count BSs per unit luminosity or per horizontal branch star
- GC: anti-correlation with density and encounter rate (Nature 2026)
- OC: correlation with age (more time = more BSs) but weak density dependence
- Diagnostic: if OCs show BS frequency rising with age but flat with density, while GCs show the inverse, the density-BS relationship is not universal — implying channel physics differs by environment, or a third process (e.g., triple dynamics, Kozai cycles) operates in one regime.

### 6. X-ray Emission (links to prior experiment)
- Method: eROSITA soft band stacking at BS positions
- GC: soft excess at BS positions would suggest magnetic activity or accretion
- OC: BSs are young enough that chromospheric activity is expected regardless of formation channel — X-ray is a weaker discriminator here
- Diagnostic: if GC BS X-ray excess correlates with C/O enrichment (accretors) but not with rotation (collision products), supports mass transfer. If excess correlates with core proximity, supports collisions.

### 7. TESS Asteroseismology (NEW)
- Method: oscillation frequency analysis of BS light curves from TESS 2-min cadence and 30-min FFIs
- Physical basis: a collision product is thoroughly mixed — nearly uniform composition throughout — while a mass-transfer accretor retains a layered structure with fresh hydrogen envelope over a processed core. These interior differences shift p-mode and g-mode frequencies measurably.
- GC limitation: 21 arcsec/pixel scale means core crowding destroys individual BS signals; only outskirts BSs in loose clusters like NGC 4372 or M4 might work
- OC advantage: NGC 6791 and NGC 6819 in TESS continuous viewing zones; sparse fields give clean BS light curves
- Diagnostic: if OC BSs show mixed-interior frequency signatures (collision-like) alongside chemically enriched ones (transfer-like), both channels confirmed in the same environment. If all OC BS frequencies indicate unmixed layered interiors, mass transfer dominates in sparse clusters — strengthening the density-dependent channel picture.
- Null result meaning: if OC BS frequencies are indistinguishable from normal main-sequence stars of the same mass, either BSs are not genuinely rejuvenated (contradicts CMD position) or asteroseismic sensitivity to mixing is lower than models predict — itself a falsifiable outcome.
- Cross-check: compare asteroseismic mixing diagnostics against C/O abundance patterns from spectroscopy on the same stars for validation

## Statistical Framework
1. Build uniform BS catalogs for all target clusters using identical selection criteria (CMD position above turnoff, UV excess where available)
2. Compute BS frequency, binary fraction, rotation distribution, abundance patterns, radial profiles per cluster
3. Fit multivariate regression: BS properties vs log(density), age, metallicity, encounter rate
4. Test for regime transitions: is there a density threshold where collision signatures appear?
5. Bayesian model comparison: collision-only, mass-transfer-only, mixed, and null (third channel) models
6. Cross-validate with independent datasets (different instruments, different clusters)
7. Asteroseismic subset: restrict to OCs in TESS CVZs; compare frequency-derived mixing profiles against spectroscopic C/O on overlapping stars

## Falsifiability
- If both GC and OC BS populations show identical binary fractions, rotation, and chemistry despite 4 orders of magnitude density difference → both collision and mass-transfer channels are weak; a third mechanism (e.g., Kozai-driven triples, stellar mergers in hierarchical systems) may dominate
- If GC BSs are chemically enriched but OC BSs are not → environment-dependent channel switching confirmed
- If OC BSs are fast rotators and GC BSs are slow → age-dependent braking masks collision signatures in GCs; collision channel may be underestimated
- If TESS OC BS frequencies show mixed interiors while spectroscopy shows C/O enrichment → both channels operate simultaneously in sparse environments; the Nature anti-correlation may reflect BS destruction, not formation suppression
- If TESS OC BS frequencies match normal MS stars → asteroseismic channel discrimination fails or BSs are not what CMD position suggests

## Open Questions
- Do triple systems (Kozai-Lidov cycles) produce BSs without requiring close binaries or collisions? Testable via RV monitoring for tertiary companions.
- Is the Nature 2026 anti-correlation an artifact of BS destruction in dense cores (collisions destroying prior BSs)? Testable via BS age distributions and asteroseismic interior ages.
- Can BS asteroseismology distinguish collision products (mixed interiors) from mass-transfer accretors (unmixed)? Kepler/TESS data on OC BSs may enable this — primary test of this updated experiment.
- Does the 21-arcsec TESS pixel scale permit any GC BS asteroseismology in outskirts, or is the OC-only restriction absolute?
