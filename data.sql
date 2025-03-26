--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5
-- Dumped by pg_dump version 16.1

-- Started on 2025-03-27 06:26:03

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

--
-- TOC entry 839 (class 1247 OID 17633)
-- Name: borrowing_status; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.borrowing_status AS ENUM (
    'BORROWED',
    'RETURNED'
);


ALTER TYPE public.borrowing_status OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 17678)
-- Name: books; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.books (
    id uuid DEFAULT gen_random_uuid() NOT NULL,
    title character varying(255) NOT NULL,
    author character varying(255) NOT NULL,
    published_year integer NOT NULL,
    stock integer DEFAULT 0 NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    isbn character varying(13) NOT NULL
);


ALTER TABLE public.books OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 17703)
-- Name: borrowings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.borrowings (
    id uuid DEFAULT gen_random_uuid() NOT NULL,
    book_id uuid NOT NULL,
    member_id uuid NOT NULL,
    borrow_date date NOT NULL,
    return_date date,
    status public.borrowing_status DEFAULT 'BORROWED'::public.borrowing_status,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.borrowings OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 17691)
-- Name: members; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.members (
    id uuid DEFAULT gen_random_uuid() NOT NULL,
    name character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    phone character varying(15) NOT NULL,
    address text NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.members OWNER TO postgres;

--
-- TOC entry 3350 (class 0 OID 17678)
-- Dependencies: 214
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.books VALUES ('7ea4be05-2594-4415-acdf-43fbf1de88cd', 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 5, '2025-03-26 20:38:13.755017', '2025-03-26 20:38:13.755017', '9780743273565');
INSERT INTO public.books VALUES ('63624d4d-0e41-45a1-be8f-2ceb0af7929c', 'To Kill a Mockingbird', 'Harper Lee', 1960, 3, '2025-03-26 20:38:13.755017', '2025-03-26 20:38:13.755017', '9780446310789');
INSERT INTO public.books VALUES ('faf5bb99-7ec9-4755-a5ac-12689d37db01', '1984', 'George Orwell', 1949, 4, '2025-03-26 20:38:13.755017', '2025-03-26 20:38:13.755017', '9780451524935');
INSERT INTO public.books VALUES ('e5d7efc2-58d4-4b55-85d0-ca338e40671e', 'Life of Pi', 'Yann Martel', 2001, 5, '2025-03-26 20:38:13.755017', '2025-03-26 20:38:13.755017', '9780156027328');
INSERT INTO public.books VALUES ('59ce4485-d86a-4613-a615-6e13bc13a7a4', 'Python Programming', 'John Doe', 2022, 5, '2025-03-26 20:51:18.046361', '2025-03-26 20:51:18.046361', '1234567890123');
INSERT INTO public.books VALUES ('d2a53fe7-f343-4425-a294-1080db747b89', 'Javasripct Programming', 'John Doe', 2023, 5, '2025-03-26 20:56:38.037341', '2025-03-26 20:56:38.037341', '1234567890112');
INSERT INTO public.books VALUES ('30037954-4657-40d4-89a9-51fa9a29851e', 'Pride and Prejudice', 'Jane Austen', 1813, 6, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780141439518');
INSERT INTO public.books VALUES ('9484c382-b779-474c-9bb5-b93e0640cc18', 'The Catcher in the Rye', 'J.D. Salinger', 1951, 3, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780316769488');
INSERT INTO public.books VALUES ('70c8149a-75fc-4b5e-abc8-81a8cbe63fd0', 'The Hobbit', 'J.R.R. Tolkien', 1937, 7, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780547928227');
INSERT INTO public.books VALUES ('746554bf-cb29-4865-98b6-7e3ffdf2e4f9', 'The Da Vinci Code', 'Dan Brown', 2003, 4, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780307474278');
INSERT INTO public.books VALUES ('e3aaa120-ef18-4764-b2f9-910d3b1552c1', 'Brave New World', 'Aldous Huxley', 1932, 4, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780060850524');
INSERT INTO public.books VALUES ('186f91b2-0fd9-4ab2-b5f2-52f3944c0e6a', 'The Lord of the Rings', 'J.R.R. Tolkien', 1954, 6, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780618640157');
INSERT INTO public.books VALUES ('312a7aa8-cec5-4372-b74d-e94f0f932b47', 'Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 1997, 7, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780590353427');
INSERT INTO public.books VALUES ('fa4f7d52-c979-495e-9928-58404e768267', 'The Chronicles of Narnia', 'C.S. Lewis', 1950, 5, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780066238501');
INSERT INTO public.books VALUES ('31bc144c-d71c-44d2-9473-5110b72fea10', 'One Hundred Years of Solitude', 'Gabriel García Márquez', 1967, 3, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780060883287');
INSERT INTO public.books VALUES ('4b494d07-57c9-4bf2-a66d-9112b881b06e', 'The Hunger Games', 'Suzanne Collins', 2008, 6, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780439023481');
INSERT INTO public.books VALUES ('d4b2d02e-2949-4553-ba1b-a2c72f5491db', 'The Road', 'Cormac McCarthy', 2006, 4, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780307387899');
INSERT INTO public.books VALUES ('36953bf2-3f58-4291-864c-bef6bad7ea0d', 'The Kite Runner', 'Khaled Hosseini', 2003, 5, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9781594631931');
INSERT INTO public.books VALUES ('b05bc88e-2a2d-4e6f-8798-33dc307d49b2', 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 2005, 4, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780307949486');
INSERT INTO public.books VALUES ('07c67eef-28fd-419f-aa1a-33e85cd32a61', 'The Book Thief', 'Markus Zusak', 2005, 6, '2025-03-26 21:24:13.230918', '2025-03-26 21:24:13.230918', '9780375842207');
INSERT INTO public.books VALUES ('47996326-9141-432e-8853-8f890475452d', 'The Alchemist', 'Paulo Coelho', 1988, 1, '2025-03-26 21:24:13.230918', '2025-03-26 23:44:14.12515', '9780062315007');
INSERT INTO public.books VALUES ('ebde10a9-1d88-4c65-aeb2-9283142c9a30', 'Golang Programming', 'John Doe', 2023, 5, '2025-03-27 00:14:51.1584', '2025-03-27 00:14:51.1584', '1239856789018');
INSERT INTO public.books VALUES ('960bba28-3366-48ed-b5da-85a0aa03f134', 'Java Programming', 'John Doe', 2023, 5, '2025-03-27 00:17:36.492542', '2025-03-27 00:17:36.492542', '1239856789918');
INSERT INTO public.books VALUES ('931b1eb4-d2aa-407e-a1cb-f33562900253', 'Ruby Programming', 'John Doe', 2023, 5, '2025-03-27 00:21:29.500851', '2025-03-27 00:21:29.500851', '123985675918');
INSERT INTO public.books VALUES ('df1c35e9-613c-465b-8bf0-f8c3d22a5f1c', 'dart Programming', 'John Doe', 2023, 5, '2025-03-27 00:22:23.410765', '2025-03-27 00:22:23.410765', '123985675218');
INSERT INTO public.books VALUES ('493655ba-a5c4-49e2-8c0d-5d0af2eef9db', 'The Little Prince', 'Antoine de Saint-Exupéry', 1943, 6, '2025-03-26 21:24:13.230918', '2025-03-27 06:06:35.785006', '9780156012195');


--
-- TOC entry 3352 (class 0 OID 17703)
-- Dependencies: 216
-- Data for Name: borrowings; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.borrowings VALUES ('e1613c36-9e19-4e80-8a0b-857d3492aacf', '63624d4d-0e41-45a1-be8f-2ceb0af7929c', '47823141-e84c-47d9-b401-31747666de11', '2024-11-22', '2024-11-29', 'RETURNED', '2025-03-26 20:42:26.003537', '2025-03-26 20:42:26.003537');
INSERT INTO public.borrowings VALUES ('4dac649c-0212-4249-93c5-4eed14a89bc8', 'e5d7efc2-58d4-4b55-85d0-ca338e40671e', 'bdb25648-17ee-4a9a-931f-3c2664845f2e', '2024-11-24', NULL, 'BORROWED', '2025-03-26 20:42:26.003537', '2025-03-26 20:42:26.003537');
INSERT INTO public.borrowings VALUES ('b5efd715-dd2d-4c09-8a1f-5a3a55f5cb35', 'faf5bb99-7ec9-4755-a5ac-12689d37db01', 'db994394-cba9-4968-bad9-03b3658a1631', '2024-12-10', '2024-12-17', 'RETURNED', '2025-03-26 20:42:26.003537', '2025-03-26 20:42:26.003537');
INSERT INTO public.borrowings VALUES ('04174daa-86ad-4900-9da6-d653c8a5fabf', '59ce4485-d86a-4613-a615-6e13bc13a7a4', 'f7579f9a-7b55-4828-b6a0-6308d6dd2c07', '2025-03-26', NULL, 'BORROWED', '2025-03-26 20:51:18.058188', '2025-03-26 20:51:18.058188');
INSERT INTO public.borrowings VALUES ('56ca16cc-6944-4d01-b7f5-48eef0c26b8a', '493655ba-a5c4-49e2-8c0d-5d0af2eef9db', 'e319823e-2051-414d-a8a4-b826656446fe', '2025-03-26', NULL, 'BORROWED', '2025-03-26 22:59:09.644917', '2025-03-26 22:59:09.644917');
INSERT INTO public.borrowings VALUES ('15186921-fad7-4fca-b081-c1ac96e6f36f', '493655ba-a5c4-49e2-8c0d-5d0af2eef9db', 'e319823e-2051-414d-a8a4-b826656446fe', '2025-03-26', NULL, 'BORROWED', '2025-03-26 22:59:19.643801', '2025-03-26 22:59:19.643801');
INSERT INTO public.borrowings VALUES ('13edfa79-80be-4094-880a-6ed2422ed09a', '47996326-9141-432e-8853-8f890475452d', 'e319823e-2051-414d-a8a4-b826656446fe', '2025-03-26', '2025-03-26', 'RETURNED', '2025-03-26 22:55:15.48367', '2025-03-26 23:44:14.12515');
INSERT INTO public.borrowings VALUES ('282d1806-6984-46f1-b349-b9642440ce6e', 'ebde10a9-1d88-4c65-aeb2-9283142c9a30', '772b8169-b6e6-4f98-885a-49ec1fe468e8', '2025-03-27', NULL, 'BORROWED', '2025-03-27 00:14:51.178215', '2025-03-27 00:14:51.178215');
INSERT INTO public.borrowings VALUES ('f9246bf3-72cb-4c97-a909-3da38a664b61', '960bba28-3366-48ed-b5da-85a0aa03f134', '51767407-c0fb-4c4a-a09f-fd622d3e39b7', '2025-03-27', NULL, 'BORROWED', '2025-03-27 00:17:36.515045', '2025-03-27 00:17:36.515045');
INSERT INTO public.borrowings VALUES ('dc20f99e-30bb-4814-9271-458c78830776', '931b1eb4-d2aa-407e-a1cb-f33562900253', '86ade36e-492e-47da-82f0-e5367f98ac28', '2025-03-27', NULL, 'BORROWED', '2025-03-27 00:21:29.511416', '2025-03-27 00:21:29.511416');
INSERT INTO public.borrowings VALUES ('43e5d590-fecb-4860-a5d3-16f5298ed786', 'df1c35e9-613c-465b-8bf0-f8c3d22a5f1c', '8153d609-5c3d-4ff8-b607-0c3d7bad3a61', '2025-03-27', NULL, 'BORROWED', '2025-03-27 00:22:23.4181', '2025-03-27 00:22:23.4181');
INSERT INTO public.borrowings VALUES ('09c8e05f-44fc-48d2-acde-318b1a883219', '493655ba-a5c4-49e2-8c0d-5d0af2eef9db', 'e319823e-2051-414d-a8a4-b826656446fe', '2025-03-27', '2025-03-27', 'RETURNED', '2025-03-27 06:02:00.94599', '2025-03-27 06:06:35.785006');


--
-- TOC entry 3351 (class 0 OID 17691)
-- Dependencies: 215
-- Data for Name: members; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.members VALUES ('47823141-e84c-47d9-b401-31747666de11', 'John Doe', 'john.doe@email.com', '081234567890', '123 Main St, City', '2025-03-26 20:39:12.690207', '2025-03-26 20:39:12.690207');
INSERT INTO public.members VALUES ('db994394-cba9-4968-bad9-03b3658a1631', 'Jane Smith', 'jane.smith@email.com', '081234567891', '456 Oak Ave, Town', '2025-03-26 20:39:12.690207', '2025-03-26 20:39:12.690207');
INSERT INTO public.members VALUES ('bdb25648-17ee-4a9a-931f-3c2664845f2e', 'Nicole King', 'nicole.k@email.com', '081234567809', '135 Port Ave, Area', '2025-03-26 20:39:12.690207', '2025-03-26 20:39:12.690207');
INSERT INTO public.members VALUES ('f7579f9a-7b55-4828-b6a0-6308d6dd2c07', 'Alice', 'alice@example.com', '+628123456789', '123 Main St', '2025-03-26 20:51:18.046361', '2025-03-26 20:51:18.046361');
INSERT INTO public.members VALUES ('e319823e-2051-414d-a8a4-b826656446fe', 'Perdana Putro Harwanto', 'perdana@mail.com', '+628212345874', 'Gunung Batu', '2025-03-26 22:22:43.788947', '2025-03-26 22:22:43.788947');
INSERT INTO public.members VALUES ('4f506ad8-9ee5-4de9-93f4-59ed41d77245', 'Perdana Putro ', 'perdana2@mail.com', '628212345874', 'Gunung Batu', '2025-03-26 22:24:42.598052', '2025-03-26 22:24:42.598052');
INSERT INTO public.members VALUES ('7c6bc814-c8ad-4af2-96d5-3914c6b72f08', 'Perdana Putro H', 'perdana3@mail.com', '08212345874', 'Gunung Batu', '2025-03-26 22:24:55.540098', '2025-03-26 22:24:55.540098');
INSERT INTO public.members VALUES ('772b8169-b6e6-4f98-885a-49ec1fe468e8', 'hiasa', 'hiasa@mail.com', '+62812346789', '123 Main St', '2025-03-27 00:14:51.171359', '2025-03-27 00:14:51.171359');
INSERT INTO public.members VALUES ('51767407-c0fb-4c4a-a09f-fd622d3e39b7', 'hiaswa', 'hiasa2@mail.com', '+62812346789', '123 Main St', '2025-03-27 00:17:36.507566', '2025-03-27 00:17:36.507566');
INSERT INTO public.members VALUES ('86ade36e-492e-47da-82f0-e5367f98ac28', 'hiase', 'hiasa3@mail.com', '+62812346789', '123 Main St', '2025-03-27 00:21:29.500851', '2025-03-27 00:21:29.500851');
INSERT INTO public.members VALUES ('8153d609-5c3d-4ff8-b607-0c3d7bad3a61', 'hiese', 'hiasa4@mail.com', '+62812346789', '123 Main St', '2025-03-27 00:22:23.410765', '2025-03-27 00:22:23.410765');
INSERT INTO public.members VALUES ('cbdcf96c-4648-44ea-a7ab-74b0bd9a1db2', 'Syifa Chofifa', 'gyifa@gmail.com', '082123458784', 'Gunung Batu', '2025-03-27 05:41:30.960629', '2025-03-27 05:41:30.960629');


--
-- TOC entry 3195 (class 2606 OID 17690)
-- Name: books books_isbn_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_isbn_key UNIQUE (isbn);


--
-- TOC entry 3197 (class 2606 OID 17688)
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);


--
-- TOC entry 3203 (class 2606 OID 17711)
-- Name: borrowings borrowings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrowings
    ADD CONSTRAINT borrowings_pkey PRIMARY KEY (id);


--
-- TOC entry 3199 (class 2606 OID 17702)
-- Name: members members_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_email_key UNIQUE (email);


--
-- TOC entry 3201 (class 2606 OID 17700)
-- Name: members members_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_pkey PRIMARY KEY (id);


--
-- TOC entry 3204 (class 1259 OID 17723)
-- Name: idx_borrowing_book; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_borrowing_book ON public.borrowings USING btree (book_id);


--
-- TOC entry 3205 (class 1259 OID 17722)
-- Name: idx_borrowing_member_status; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_borrowing_member_status ON public.borrowings USING btree (member_id, status);


--
-- TOC entry 3206 (class 2606 OID 17712)
-- Name: borrowings borrowings_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrowings
    ADD CONSTRAINT borrowings_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(id);


--
-- TOC entry 3207 (class 2606 OID 17717)
-- Name: borrowings borrowings_member_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrowings
    ADD CONSTRAINT borrowings_member_id_fkey FOREIGN KEY (member_id) REFERENCES public.members(id);


-- Completed on 2025-03-27 06:26:03

--
-- PostgreSQL database dump complete
--

