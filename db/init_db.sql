-- Table: public.recipe

-- DROP TABLE IF EXISTS public.recipe;

CREATE TABLE IF NOT EXISTS public.recipe
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    name character varying(80) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "RECIPE_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.recipe
    OWNER to postgres;

INSERT INTO public.recipe(name)
VALUES ('Crozineuftiflette'),('Quiche lorraine'),('Croque monsieur');