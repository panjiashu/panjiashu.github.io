(function (global) {
  "use strict";

  const STORAGE_KEY = "homepage-language";

  function normalizeLanguage(value) {
    return value === "zh" ? "zh" : "en";
  }

  function readLanguagePreference(storage) {
    try {
      return normalizeLanguage(storage && storage.getItem(STORAGE_KEY));
    } catch (_error) {
      return "en";
    }
  }

  function saveLanguagePreference(storage, language) {
    try {
      if (storage) storage.setItem(STORAGE_KEY, normalizeLanguage(language));
    } catch (_error) {
      // Language switching remains functional when storage is unavailable.
    }
  }

  function applyLanguage(document, language) {
    const selected = normalizeLanguage(language);
    document.documentElement.lang = selected === "zh" ? "zh-CN" : "en";
    document.documentElement.dataset.language = selected;

    document.querySelectorAll("[data-lang]").forEach((element) => {
      element.hidden = element.dataset.lang !== selected;
    });

    document.querySelectorAll("[data-language-choice]").forEach((button) => {
      const active = button.dataset.languageChoice === selected;
      button.setAttribute("aria-pressed", String(active));
      button.classList.toggle("is-active", active);
    });

    return selected;
  }

  function initLanguage(document, storage) {
    let selected = applyLanguage(document, readLanguagePreference(storage));

    document.querySelectorAll("[data-language-choice]").forEach((button) => {
      button.addEventListener("click", () => {
        selected = applyLanguage(document, button.dataset.languageChoice);
        saveLanguagePreference(storage, selected);
      });
    });

    return selected;
  }

  const api = {
    STORAGE_KEY,
    applyLanguage,
    initLanguage,
    normalizeLanguage,
    readLanguagePreference,
    saveLanguagePreference,
  };

  if (typeof module !== "undefined" && module.exports) module.exports = api;
  global.HomeLanguage = api;

  if (typeof document !== "undefined") {
    const start = () => initLanguage(document, global.localStorage);
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", start, { once: true });
    } else {
      start();
    }
  }
})(typeof globalThis !== "undefined" ? globalThis : this);
