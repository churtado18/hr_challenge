SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE employees_hired_by_quarter
(
    @anio INT
)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON
    
		SELECT 
			D.department,
			J.job,
			COUNT(CASE WHEN DATEPART(QUARTER, E.[datetime]) = 1 THEN 1 END) AS q1,
			COUNT(CASE WHEN DATEPART(QUARTER, E.[datetime]) = 2 THEN 1 END) AS q2,
			COUNT(CASE WHEN DATEPART(QUARTER, E.[datetime]) = 3 THEN 1 END) AS q3,
			COUNT(CASE WHEN DATEPART(QUARTER, E.[datetime]) = 4 THEN 1 END) AS q4			
		FROM dbo.hired_employees E
		INNER JOIN dbo.departments D ON E.department_id = D.id
		INNER JOIN dbo.jobs J ON E.job_id = J.id
		WHERE YEAR(E.[datetime]) = @anio 
		GROUP BY D.department, J.job
		ORDER BY D.department
	END
GO
