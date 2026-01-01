# 離散傅立葉轉換實作 (Discrete Fourier Transform Implementation)

本專案為 GitHub 作業，旨在不使用任何第三方科學運算套件（如 NumPy, SciPy）的情況下，使用 Python 原生語法實作 **離散傅立葉正轉換 (DFT)** 與 **逆轉換 (IDFT)**。

## 1. 數學原理

傅立葉轉換的核心在於將時域 (Time Domain) 的訊號轉換為頻域 (Frequency Domain) 的表示。

### 正轉換 (DFT)
$$X_k = \sum_{n=0}^{N-1} x_n \cdot e^{-i \frac{2\pi}{N} kn}$$

### 逆轉換 (IDFT)
$$x_n = \frac{1}{N} \sum_{k=0}^{N-1} X_k \cdot e^{i \frac{2\pi}{N} kn}$$

其中：
- $N$ 是訊號的總樣本數。
- $x_n$ 是時域中的第 $n$ 個樣本。
- $X_k$ 是頻域中的第 $k$ 個頻譜分量。

---

## 2. 檔案結構

- `dft_implementation.py`: 包含 DFT 與 IDFT 函式的主程式。
- `README.md`: 專案說明文件。

---

## 3. 程式碼邏輯說明

本實作使用 Python 內建的 `cmath` 模組處理複數運算：

1. **`dft(x)`**: 
   - 接受一個數值列表作為輸入。
   - 使用雙重迴圈計算每個頻率 $k$ 的總和。
   - 返回一個包含複數的列表，代表頻譜。

2. **`idft(X)`**:
   - 接受頻譜列表作為輸入。
   - 將指數符號轉為正值，並在計算結束後除以 $N$ 以還原訊號強度。
   - 返回還原後的時域訊號。

---

## 4. 如何執行

確保你已安裝 Python 3，然後在終端機執行：

```bash
python dft_implementation.py
