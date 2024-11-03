const fs = require("fs");
const path = require("path"); // Import the path module

async function getDirSize(dirPath) {
  let totalSize = 0;
  const files = await fs.promises.readdir(dirPath);

  for (const file of files) {
    const filePath = path.join(dirPath, file);
    const stat = await fs.promises.stat(filePath);

    if (stat.isDirectory()) {
      totalSize += await getDirSize(filePath);
    } else {
      totalSize += stat.size;
    }
  }
  return totalSize;
}

function formatBytes(bytes, decimals = 2) {
  if (bytes === 0) return "0 Bytes";

  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + " " + sizes[i];
}
const userDataDir = "/Users/theinprem/Downloads";
getDirSize(userDataDir).then((size) => {
  console.log("format size\t" + formatBytes(size));
  console.log(
    `Total size of ${userDataDir}: ${size} bytes` +
      ":" +
      `${size / 1000} kilobytes` +
      +`${size / 1000000} megabytes`
  );
});
