# Project Rules

## Image Optimization
- Always ensure that any newly uploaded images (especially raw photos from mobile phones like `.HEIC`, `.JPG`, `.png`) are compressed and optimized for the web before adding them to the repository.
- Use `sips` to resize images (e.g. `sips -s format jpeg -s formatOptions 80 -Z 1920`) and compress them to `.jpg` formats.
- If the user provides an image, check its file size and explicitly offer or just execute optimization if it is over 1 Megabyte to maintain fast website loading speeds.
