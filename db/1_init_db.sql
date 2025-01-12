--
-- PostgreSQL database dump
--

-- Dumped from database version 16.6 (Ubuntu 16.6-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.6 (Ubuntu 16.6-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: ingredient; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ingredient (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    quantity_type smallint NOT NULL
);


ALTER TABLE public.ingredient OWNER TO postgres;

--
-- Name: ingredient_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.ingredient ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.ingredient_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: recipe; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recipe (
    id bigint NOT NULL,
    name character varying(80) NOT NULL,
    duration integer,
    difficulty smallint
);


ALTER TABLE public.recipe OWNER TO postgres;

--
-- Name: recipe_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.recipe ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.recipe_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: recipe_ingredient; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recipe_ingredient (
    recipe_id bigint NOT NULL,
    ingredient_id bigint NOT NULL,
    quantity integer NOT NULL
);


ALTER TABLE public.recipe_ingredient OWNER TO postgres;

--
-- Name: recipe_step; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recipe_step (
    recipe_id bigint NOT NULL,
    name character varying(80) NOT NULL,
    description character varying(500),
    "position" integer NOT NULL
);


ALTER TABLE public.recipe_step OWNER TO postgres;

--
-- Name: recipe RECIPE_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe
    ADD CONSTRAINT "RECIPE_pkey" PRIMARY KEY (id);


--
-- Name: ingredient ingredient_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ingredient
    ADD CONSTRAINT ingredient_pkey PRIMARY KEY (id);


--
-- Name: recipe_ingredient recipe_ingredient_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe_ingredient
    ADD CONSTRAINT recipe_ingredient_pkey PRIMARY KEY (recipe_id, ingredient_id);


--
-- Name: recipe_step recipe_step_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe_step
    ADD CONSTRAINT recipe_step_pkey PRIMARY KEY (recipe_id, "position");


--
-- Name: ingredient u_ingredient_name; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ingredient
    ADD CONSTRAINT u_ingredient_name UNIQUE (name);


--
-- Name: fki_fk_recipe_ingredient_to_recipe; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_fk_recipe_ingredient_to_recipe ON public.recipe_ingredient USING btree (recipe_id);


--
-- Name: recipe_ingredient fk_recipe_ingredient_to_ingredient; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe_ingredient
    ADD CONSTRAINT fk_recipe_ingredient_to_ingredient FOREIGN KEY (ingredient_id) REFERENCES public.ingredient(id);


--
-- Name: recipe_ingredient fk_recipe_ingredient_to_recipe; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe_ingredient
    ADD CONSTRAINT fk_recipe_ingredient_to_recipe FOREIGN KEY (recipe_id) REFERENCES public.recipe(id) ON DELETE CASCADE;


--
-- Name: recipe_step fk_recipe_step_to_recipe; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe_step
    ADD CONSTRAINT fk_recipe_step_to_recipe FOREIGN KEY (recipe_id) REFERENCES public.recipe(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

