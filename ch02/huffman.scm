; 树叶表示为包含符号leaf、叶中符号、权重的的表
(define (make-leaf symbol weight)
    (list `leaf symbol weight))

(define (leaf? object)
    (eq? (car object) `leaf))

(define (symbol-leaf x)
    (cadr x))

(define (weight-leaf x)
    (caddr x))

(define (make-code-tree right)
    (list left
          right
          (append (symbols left) (symbols right))
          (+ (weight left) (weight right))))