
/**
 * if branch with braces
 */
if (cond) {
    frob();
}
next();


/**
 * if branch without braces
 */
if (cond)
    frob();
next();


/**
 * if/else branch with braces
 */
if (cond) {
    foo();
} else {
    bar();
}
next();


/**
 * if/else branch without braces
 */
if (cond)
    foo();
else
    bar();
next();


/**
 * Special branch content
 */
if (cond)
    return
else
    continue
next();







