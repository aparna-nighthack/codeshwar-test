
/**
 * Debounce function to limit the rate at which a function can fire.
 * Preserves the original context and provides methods to cancel and flush calls.
 * @param {Function} func - The function to debounce.
 * @param {number} wait - The number of milliseconds to delay.
 * @return {Function} - A debounced version of the original function with cancel and flush methods.
 */
export function debounce(func, wait) {
  let timeout;
  const debounced = function(...args) {
    const context = this;
    const later = () => {
      timeout = null;
      func.apply(context, args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };

  debounced.cancel = function() {
    clearTimeout(timeout);
    timeout = null;
  };

  debounced.flush = function() {
    clearTimeout(timeout);
    func.apply(this, arguments);
    timeout = null;
  };

  return debounced;
}

/**
 * Throttle function to ensure a function is only executed at most once in a specified time period.
 * Now performs leading and trailing invocations by default, preserving the original context, and provides cancel and flush methods.
 * @param {Function} func - The function to throttle.
 * @param {number} limit - The time frame for which to suppress further calls.
 * @return {Function} - A throttled version of the original function with cancel and flush methods.
 */
export function throttle(func, limit) {
  let lastFunc;
  let lastRan;
  const throttled = function(...args) {
    const context = this;
    if (!lastRan) {
      func.apply(context, args);
      lastRan = Date.now();
    } else {
      clearTimeout(lastFunc);
      lastFunc = setTimeout(() => {
        if ((Date.now() - lastRan) >= limit) {
          func.apply(context, args);
          lastRan = Date.now();
        }
      }, limit - (Date.now() - lastRan));
    }
  };

  throttled.cancel = function() {
    clearTimeout(lastFunc);
    lastFunc = null;
    lastRan = null;
  };

  throttled.flush = function() {
    clearTimeout(lastFunc);
    func.apply(this, arguments);
    lastRan = Date.now();
    lastFunc = null;
  };

  return throttled;
}