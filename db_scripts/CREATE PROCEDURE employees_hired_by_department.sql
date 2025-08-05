SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE employees_hired_by_department
(
    @anio INT
)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON
    
		DECLARE @num_dep INT
		DECLARE @prom_anio INT

		SELECT  @num_dep = COUNT(1)
		FROM (
			SELECT COUNT(1) AS cant_depto
			FROM dbo.hired_employees E
			INNER JOIN dbo.departments D ON E.department_id = D.id
			WHERE YEAR([datetime]) = @anio
			GROUP BY E.department_id
		 ) AS T

		SELECT  @prom_anio = COUNT(1) / @num_dep
		FROM dbo.hired_employees
		WHERE YEAR([datetime]) = @anio


		SELECT D.id, D.department, COUNT(1) AS hired_number
		FROM dbo.hired_employees E
		INNER JOIN dbo.departments D ON E.department_id = D.id
		WHERE YEAR(E.[datetime]) = @anio
		GROUP BY D.id, D.department
		HAVING(COUNT(1) >= @prom_anio)
		ORDER BY 3 DESC

	END
GO
