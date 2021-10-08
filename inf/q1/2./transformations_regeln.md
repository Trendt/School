# 7.6 Umsetzung des ER-Modells

## 4 Transformationsregeln:

1. Jede Entitätsmenge wird im relationalen Modell in eine eigenständige Relation überführt.
2. Jede n:m Beziehung wird im relationalen Modell in eine eigenständige Relation überführt. Attribute dieser Relation sind die Primärschlüssel der beiden an der Beziehung beteiligten Entitätsmengen (als Fremdschlüssel), die gemeinsam den Primärschlüssel bilden, sowie ggf. Attribute der Beziehungsmenge.
3. Jede 1:n Beziehung wird im relationalen Modell ohne eine eigene Tabelle abgebildet. Dies geschieht indem der Relation mit der Kardinalität n derr Primärschlüssel mit der Kardinalität 1 als Fremdschlüssel angefügt wird. Attribute der Beziehungsmenge werden ggf. auch dieser Relation angefügt.
4. Jede 1:1 Beziehung wird im relationalen Modell ohne eine eigene Tabelle abgebildet. Dies geschieht, indem einer der an der Beziehung beteiligten Relationen der Primärschlüssel der anderen Relation als Fremdschlüssel angefügt wird. Attribute der Beziehungsmenge werden gg.f auch dieser Relation angefügt.
