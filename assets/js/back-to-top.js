document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("back-to-top");

  // Show button after scrolling down
  window.addEventListener("scroll", () => {
    if (window.scrollY > 300) {
      btn.style.display = "block";
    } else {
      btn.style.display = "none";
    }
  });

  // Smooth scroll to top
  btn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
});
