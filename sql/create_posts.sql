
CREATE TABLE posts(
    id serial NOT NULL primary key,
    title character varying NOT NULL,
    content character varying NOT NULL,
    published boolean DEFAULT false,
    created_at TIMESTAMP with time zone DEFAULT NOW()
);
