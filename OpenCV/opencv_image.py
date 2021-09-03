import cv2

gambar = cv2.imread('Pic/kurcaci.jpeg')
if not gambar is None:
  hasil = gambar.copy()

  TEBAL = 10
  HITAM = 255

  baris = hasil.shape[0]
  kolom = hasil.shape[1]

  for b in range(TEBAL):
    for k in range(kolom):
      hasil[b,k] = HITAM
  
  for b in range(baris):
    for k in range(TEBAL):
      hasil[b,k] = HITAM

  for b in range(baris):
    for k in range(kolom-TEBAL,kolom):
      hasil[b,k] = HITAM

  for b in range(baris-TEBAL,baris):
    for k in range(kolom):
      hasil[b,k] = HITAM

  cv2.namedWindow('Gambar', cv2.WINDOW_NORMAL)
  cv2.imshow('Gambar', hasil)
  cv2.waitKey(0)
  cv2.destroyAllWindows()