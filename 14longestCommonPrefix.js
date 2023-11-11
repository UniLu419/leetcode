/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
  const shortestString = findShortestString(strs);
  return findPrefix(strs, shortestString)
};

function findShortestString(strs) {
  let str = strs[0];
  for (let i = 1; i < strs.length; i++) {
    if (strs[i].length < str.length) {
      str = strs[i];
    }
  }
  return str;
}

function isPrefix(strs, str) {
  for (let i = 0; i < strs.length; i++) {
    if (!strs[i].startsWith(str)) {
      return false;
    }
  }
  return true;
}

function findPrefix(strs, str) {
  if (str.length === 0) {
    return str;
  }
  if (isPrefix(strs, str)) {
    return str;
  }
  return findPrefix(strs, str.substring(0, str.length - 1));
}