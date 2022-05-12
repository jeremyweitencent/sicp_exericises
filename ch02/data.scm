; cons car cdr的过程式实现
; (define (cons x y)
;     (define (dispatch m)
;         (cond ((= m 0) x)
;             ((= m 1) y)
;             (else (error "Argument not 0 or 1 -- CONS" m))))
;     dispatch)

; (define (car z) (z 0))
; (define (cdr z) (z 1))

; (let ((var (cons 1 2)))
;     (car var)
;     (cdr var))

(define (memq item x)
    (cond ((null? x) false)
        ((eq? item (car x)) x)
        (else (memq item (cdr x)))))

(memq 'apple '(pear banana prune))
(memq 'apple '(x (apple sauce) y apple pear))
