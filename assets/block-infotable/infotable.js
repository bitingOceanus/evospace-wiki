// @ts-check

/**
 * @param {string} tag
 * @param {{ [attr: string]: string; }} attrs
 * @param {any[]} children
 */
function e(tag, attrs, ...children) {
  const element = document.createElement(tag);
  for (const [attr, value] of Object.entries(attrs)) {
    element.setAttribute(attr, value);
  }
  for (const child of children) {
    typeof child === "string" || typeof child === "number"
      ? element.appendChild(document.createTextNode(String(child)))
      : element.appendChild(child);
  }
  return element;
}

/**
 * @param {string | number | HTMLElement} cardName text in card header
 * @param {string} imageSrc link to image
 * @param {(string | number)[][]} descriptionParts info for table
 */
function createCard(cardName, imageSrc, descriptionParts) {
  return e("div", { class: "card" },
    e("div", { class: "card__header" }, cardName),
    e("div", {},
      e("img", { src: imageSrc, class: "card__img" }),
    ),
    e("div", { class: "table" }, ...descriptionParts.map(([partName, _, value]) => {
      const tableRow = [String(partName), value].filter(Boolean).map(text => e("span", {}, text));
      return e("div", { class: "table__row" }, ...tableRow)
    }))
  );
}

var path = window.location.pathname;
var page = path.split("/").pop()?.replace(".md", "") ?? "Unknown";

const card = createCard(page, "./assets/icons/T_" + page, [
  ["Boiler", "description_machines"],
  ["HeatInput", "common"],
  ["FluidInput", "common"],
  ["FluidOutput", "common"],
  ["power_output", "common", 4000],
]);

document.insertBefore(card, document.querySelector("#git-wiki-toc"));