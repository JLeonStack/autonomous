import { describe, expect, test } from "bun:test";
import { wordCount } from "./word-count";

describe("wordCount", () => {
  test("counts words separated by single spaces", () => {
    expect(wordCount("hello world")).toBe(2);
  });

  test("ignores leading and trailing whitespace", () => {
    expect(wordCount("  hello world  ")).toBe(2);
  });

  test("collapses repeated whitespace between words", () => {
    expect(wordCount("hello    world")).toBe(2);
  });

  test("treats any whitespace character as a separator", () => {
    expect(wordCount("a\tb\nc\r\nd")).toBe(4);
  });

  test("returns 0 for an empty string", () => {
    expect(wordCount("")).toBe(0);
  });

  test("returns 0 for a whitespace-only string", () => {
    expect(wordCount("   \t\n  ")).toBe(0);
  });

  test("counts a single word", () => {
    expect(wordCount("hello")).toBe(1);
  });
});
