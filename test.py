import imageio.v3 as iio
import numpy as np

# Create a new GIF file and open it for writing
filename = 'example.gif'
writer = iio.imopen(filename, 'w')

# Loop through the frames and write each one to the file
for i in range(10):
    # Create a new frame (replace this with your own image data)
    frame = 255 * np.random((100, 100, 3), dtype=np.uint8)
    frame[i % 3, :, :] = 0
    
    # Write the frame to the file
    writer.write(frame)

# Close the writer to finalize the file
writer.close()