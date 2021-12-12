const stories = document.getElementsByClassName("stories")[0];
stories.addEventListener("wheel", (e) => {
  stories.scrollLeft += e.deltaY;
});
// main work for story
const story = document.getElementsByClassName("story"); // ==> container of story
console.log(story);
const main = document.getElementsByClassName("main_story")[0]; // ==> full screen story
const story_image = document.getElementById("story_image"); //==> main story
const storY = document.getElementById("story"); //==> full screen stroy
Array.from(story).forEach((element) => {
  element.addEventListener("click", () => {
    main.style.display = "block";
    console.log(element.childNodes);
    let src = element.childNodes[1].src;
    console.log(src);
    storY.setAttribute("src", src);
  });
});
main.onclick = () => {
  main.style.display = "none";
};
