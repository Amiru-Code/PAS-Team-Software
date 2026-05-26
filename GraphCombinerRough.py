from PIL import Image

# Load your four graph images (must be the same pixel dimensions)
img1 = Image.open("Figure_1.png").convert("RGBA")
img2 = Image.open("Figure_2.png").convert("RGBA")
img3 = Image.open("Figure_3.png").convert("RGBA")
img4 = Image.open("Atmospheric.png").convert("RGBA")

# Blend them together sequentially using 50% opacity for the overlays
blend1 = Image.blend(img1, img2, alpha=0.5)
blend2 = Image.blend(blend1, img3, alpha=0.5)
final_overlay = Image.blend(blend2, img4, alpha=0.5)

# Save and show the result
final_overlay.save("combined_graph.png")
final_overlay.show()