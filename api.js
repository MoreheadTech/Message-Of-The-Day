const fs = require("fs");
const express = require("express");
const app = express();

app.use(express.json());

app.get("/motd", (req, res) => {
  fs.readFile("motd.txt", "utf8", (err, data) => {
    if (err) {
      console.error("Error reading file:", err);
      return res.status(500).json({ error: "Could not read MOTD" });
    }

    const motd = data.trim();
    res.json({ motd });
  });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`API started on port ${PORT}`);
});
