const fs = require('fs');
const path = require('path');

function getVideoNames(folderPath) {
  try {
    const videoFiles = fs.readdirSync(folderPath).filter((file) => {
      const extension = path.extname(file).toLowerCase();
      return ['.mp4', '.avi', '.mov', '.mkv'].includes(extension);
    });

    const videoNames = videoFiles.map((videoFile) => {
      return path.parse(videoFile).name;
    });

    return videoNames;
  } catch (error) {
    console.error('An error occurred:', error.message);
    return [];
  }
}

// Usage
const folderPath = 'folder path'; // Replace with the path to your videos folder

const videoNames = getVideoNames(folderPath);
console.log('Video names:', videoNames);

// Generate a text file with the video names
const outputFilePath = 'video_names.txt'; // Name of the output text file

try {
  const outputData = videoNames.join('\n');
  fs.writeFileSync(outputFilePath, outputData);
  console.log(`Video names saved to ${outputFilePath}`);
} catch (error) {
  console.error('An error occurred while saving the file:', error.message);
}
