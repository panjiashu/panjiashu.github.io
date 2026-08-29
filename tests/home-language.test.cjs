const test = require("node:test");
const assert = require("node:assert/strict");

const { applyLanguage, readLanguagePreference } = require("../assets/js/home-language.js");

function fakeDocument() {
  const localized = [
    { dataset: { lang: "en" }, hidden: false },
    { dataset: { lang: "zh" }, hidden: true },
  ];
  const toggles = [
    {
      dataset: { languageChoice: "en" },
      attributes: {},
      classList: { toggle() {} },
      setAttribute(name, value) {
        this.attributes[name] = value;
      },
    },
    {
      dataset: { languageChoice: "zh" },
      attributes: {},
      classList: { toggle() {} },
      setAttribute(name, value) {
        this.attributes[name] = value;
      },
    },
  ];

  return {
    documentElement: { lang: "en", dataset: {} },
    localized,
    toggles,
    querySelectorAll(selector) {
      return selector === "[data-lang]" ? localized : toggles;
    },
  };
}

test("reads a saved Chinese preference", () => {
  const storage = { getItem: () => "zh" };
  assert.equal(readLanguagePreference(storage), "zh");
});

test("falls back to English for missing or invalid preferences", () => {
  assert.equal(readLanguagePreference({ getItem: () => null }), "en");
  assert.equal(readLanguagePreference({ getItem: () => "ja" }), "en");
  assert.equal(
    readLanguagePreference({
      getItem: () => {
        throw new Error("blocked");
      },
    }),
    "en"
  );
});

test("applies Chinese content and accessible toggle state", () => {
  const document = fakeDocument();

  applyLanguage(document, "zh");

  assert.equal(document.documentElement.lang, "zh-CN");
  assert.equal(document.documentElement.dataset.language, "zh");
  assert.equal(document.localized[0].hidden, true);
  assert.equal(document.localized[1].hidden, false);
  assert.equal(document.toggles[0].attributes["aria-pressed"], "false");
  assert.equal(document.toggles[1].attributes["aria-pressed"], "true");
});
