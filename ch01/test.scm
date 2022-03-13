; (define (fib n)
;     (cond   ((= n 0) 0)
;             ((= n 1) 1)
;             (else   (+ (fib (- n 1))
;                     (fib (- n 2))))))

; (fib 5)

(define (averange a b)
    (/ (+ a b) 2))

; 平均阻尼
(define (averange-damp f)
    (lambda (x) (averange x (f x))))

; ((averange-damp square) 10)

(define tolerance 0.000001)

(define (fixed-point f first-guess)
    (define (close-enough? v1 v2)
        (< (abs (- v1 v2)) tolerance))
    (define (try guess)
        (let ((next (f guess)))
            (if (close-enough? guess next)
                next
                (try next))))
    (try first-guess))
    

; 高阶函数
(define (fixed-point-of-transform g transform guess)
    (fixed-point (transform g) guess))

(define (sqrt x)
    (fixed-point-of-transform (lambda (y) (/ x y))
        averange-damp 1.0))

(sqrt 4)
