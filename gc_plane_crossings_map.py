import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Impact points: (name, crossing Myr ago, distance kpc, contour radius deg,
# distance unc %, gal_l approx, gal_b approx, inclination deg, notes)
# Source: Prokhorov et al. 2008 (arXiv:0811.3106), FE potential.
# Inclinations are estimates derived from published orbital elements
# (Vasiliev & Baumgardt 2021 / Bajkova & Bobylev 2020), not direct
# outputs of the Prokhorov integration.
clusters = [
    ("NGC 6397", 3.7, 2.6, 3.0, 12, 338.2, -12.0, 52, "tightest; Ara; core-collapsed"),
    ("NGC 3201", 5.5, 2.5, 7.0, 22, 277.2, +8.6, 78, "retrograde; Vela"),
    ("NGC 6838 (M71)", 15.6, 4.5, 6.0, 20, 56.7, -4.6, 15, "low-incl; Sagitta"),
    ("NGC 6752", 29.4, 2.8, 12.0, 25, 341.2, -25.6, 60, "Pavo"),
    ("NGC 1851", 43.2, 2.5, 14.0, 30, 244.5, -35.0, 62, "Columba"),
    ("NGC 104 (47 Tuc)", 48.8, 2.2, 16.0, 30, 305.9, -44.9, 34, "Tucana"),
]

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='aitoff')
ax.grid(True, alpha=0.4, linestyle='--')

# Galactic plane (b = 0)
l = np.linspace(-np.pi, np.pi, 1000)
ax.plot(l, np.zeros_like(l), 'k-', lw=1.5, alpha=0.7, label='Galactic plane (b=0)')

# Sun
ax.plot(0, 0, 'y*', ms=18, label='Sun', zorder=5)

for name, t, d, r, du, gl, gb, inc, note in clusters:
    lon = np.radians(gl - 180)  # aitoff: l=0 at center
    lat = np.radians(gb)
    ms = 40 + r * 8
    color = plt.cm.plasma(t / 55.0)
    ax.scatter(lon, lat, s=ms, c=[color], edgecolors='white', linewidths=1.2, zorder=4, alpha=0.85)
    circ = Circle((lon, lat), np.radians(r), fill=False, edgecolor=color, lw=1.5, ls='--', alpha=0.6)
    ax.add_patch(circ)
    ax.annotate(f"{name}\n{t} Myr ago\n{d} kpc, incl {inc} deg\n{note}",
                xy=(lon, lat),
                xytext=(lon + np.radians(8), lat + np.radians(6 if gb > 0 else -10)),
                fontsize=7.5, ha='left', color='white',
                arrowprops=dict(arrowstyle='->', color='white', lw=0.8),
                bbox=dict(boxstyle='round,pad=0.3', fc='black', ec='white', alpha=0.6))

# NGC 6231 — ruled-out remnant candidate for NGC 6397
l6231 = np.radians(343.46 - 180)
b6231 = np.radians(1.186)
ax.scatter(l6231, b6231, s=120, marker='X', c='red', edgecolors='white', lw=1, zorder=6,
           label='NGC 6231 (ruled out, 0.6 kpc off contour)')
ax.annotate("NGC 6231\n(ruled out)", xy=(l6231, b6231),
            xytext=(l6231 - np.radians(15), b6231 + np.radians(12)),
            fontsize=7.5, color='red', arrowprops=dict(arrowstyle='->', color='red', lw=0.8))

# Search corridor: |b| < 5 deg along the plane, spanning the contour longitudes
lons_cov = [338.2, 277.2, 56.7, 341.2, 244.5, 305.9]
lmin, lmax = min(lons_cov) - 20, max(lons_cov) + 20
band_l = np.linspace(np.radians(lmin - 180), np.radians(lmax - 180), 200)
for db in [np.radians(5), np.radians(-5)]:
    ax.plot(band_l, np.full_like(band_l, db), 'c-', lw=1.2, alpha=0.5)
ax.fill_between(band_l, -np.radians(5), np.radians(5), color='cyan', alpha=0.08,
                 label='Search corridor |b|<5 deg')

ax.set_title("Globular Cluster Galactic Plane Crossings near the Sun\n"
             "(Prokhorov et al. 2008; impact points with 90% contours)",
             fontsize=13, pad=20)
ax.legend(loc='lower left', fontsize=8, framealpha=0.7)

txt = ("Nearest crossings (time / distance / contour / inclination):\n"
       "NGC 6397: 3.7 Myr / 2.6 kpc / 3 deg / ~52 deg\n"
       "NGC 3201: 5.5 Myr / 2.5 kpc / 7 deg / ~78 deg (retrograde)\n"
       "M71: 15.6 Myr / 4.5 kpc / 6 deg / ~15 deg\n"
       "NGC 6752: 29.4 Myr / 2.8 kpc / 12 deg / ~60 deg\n"
       "NGC 1851: 43.2 Myr / 2.5 kpc / 14 deg / ~62 deg\n"
       "47 Tuc: 48.8 Myr / 2.2 kpc / 16 deg / ~34 deg\n"
       "Best IR/X-ray search targets: NGC 6397 & NGC 3201 corridors\n"
       "(pre-main-sequence signatures <10 Myr old)")
fig.text(0.02, 0.02, txt, fontsize=7.5, family='monospace', va='bottom',
         bbox=dict(boxstyle='round', fc='black', ec='gray', alpha=0.75))

plt.tight_layout()
plt.savefig('gc_plane_crossings_map.png', dpi=160, bbox_inches='tight', facecolor='black')
print("Map saved: gc_plane_crossings_map.png")
