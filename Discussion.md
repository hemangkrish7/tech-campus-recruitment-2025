# Discussion.md

## Solutions Considered

### 1️⃣ Line-by-Line Streaming (Final Choice)
- Reads the file line by line instead of loading it into memory.
- Works well with large files (1 TB) without high RAM usage.
- Uses simple string comparison to extract logs.

### 2️⃣ Indexing with Seek (Preprocessing Required)
- Creates an index mapping dates to byte offsets.
- Allows direct seeking to the relevant section.
- Faster queries but requires extra preprocessing time and storage.

### 3️⃣ Parallel Processing (Complex but Fast)
- Uses multiple processes to scan different parts of the file.
- Faster but needs splitting the log file into chunks.
- Harder to implement and may have synchronization issues.

### 4️⃣ Grep-Based Approach (OS-Dependent)
- Uses `grep "YYYY-MM-DD"` for quick extraction.
- Very fast but works only on Unix-based systems.
- Not portable across different platforms.

---

## **Final Solution Summary**
We chose **line-by-line streaming** because it provides:
✅ **Low memory usage** (does not load the entire file).  
✅ **Simplicity** (easy to implement and debug).  
✅ **Cross
