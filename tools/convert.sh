#!/usr/bin/env bash

substitute() {
    local indent label template_file generated_file
    indent="$1"
    label="$2"
    template_file="$3"
    generated_file="$4"
    shift 4

    local head tail
    head="<editor-fold desc=\"$label\">\$"
    tail="<\\/editor-fold>\$"
    echo "Updating section '$label' in '$template_file'"
    sed -f /dev/stdin -i '' "$generated_file" <<EOF
#!/usr/bin/env sed
s/^/$indent/
EOF
    sed -f /dev/stdin -i '' "$template_file" <<EOF
#!/usr/bin/env sed
/${head}/,/${tail}/ {
  /${head}/ {
    p
    r $generated_file
  }
  /${tail}/ p
  d
}
EOF
    rm "$generated_file"
}

build_dir="$PWD/build/ogit"
gen_dir="$build_dir/generated"
dst_dir="$PWD/src"
saxon_src_url='https://repo1.maven.org/maven2/net/sf/saxon/Saxon-HE/9.9.1-8/Saxon-HE-9.9.1-8.jar'
src_url='https://graphit.co/schemas/graphit-ontology.ttl'
ttl_file="$build_dir/graphit-ontology-$(date +%Y-%m-%d).ttl"
rdf_file="$build_dir/graphit-ontology-$(date +%Y-%m-%d).rdf"
jar_file='libs/saxon9he.jar'
xsl_file='tools/python.xslt'

do_download() {
  echo 'Downloading '\''graphit-ontology.ttl'\''...'
  curl "$src_url" > "$ttl_file"
  if [ ! -d "$(dirname -- "$jar_file")" ]; then
    mkdir -p "$(dirname -- "$jar_file")"
  fi
  if [ ! -f "$jar_file" ]; then
    curl "$saxon_src_url" > "$jar_file"
  fi
}

do_convert() {
  echo "Converting to RDF..."
  # ./venv/bin/python3 ttl2rdf.py > "$rdf_file" < "$ttl_file"
  ./venv/bin/pipenv run rdfpipe -o xml "$ttl_file" > "$rdf_file"
}

do_generate() {
  echo 'Generating sources...'
  if [ ! -d "$gen_dir" ]; then
    mkdir -p "$gen_dir"
  fi
  java -jar "$jar_file" "-xsl:$xsl_file" "-s:$1" "-o:$gen_dir/dummy.py"
}

do_update() {
  echo 'Updating sources...'

  target_dir="$dst_dir/arago/ogit"
  target_file="$target_dir/data.py"
  substitute '    ' 'generated attribute data'     "$target_file"  "$gen_dir/Attribute.data.generated.py"
  substitute '    ' 'generated entity data'        "$target_file"     "$gen_dir/Entity.data.generated.py"
  substitute '    ' 'generated entity refs'        "$target_file"     "$gen_dir/Entity.refs.generated.py"
  substitute '    ' 'generated namespace data'     "$target_file"  "$gen_dir/Namespace.data.generated.py"
  substitute '    ' 'generated verb data'          "$target_file"       "$gen_dir/Verb.data.generated.py"
  target_file="$target_dir/__init__.py"
  substitute '    ' 'generated attribute members'  "$target_file"  "$gen_dir/Attribute.members.generated.py"
  substitute '    ' 'generated entity members'     "$target_file"     "$gen_dir/Entity.members.generated.py"
  substitute '    ' 'generated namespace members'  "$target_file"  "$gen_dir/Namespace.members.generated.py"
  substitute '    ' 'generated verb members'       "$target_file"       "$gen_dir/Verb.members.generated.py"
}

[ -d "$build_dir" ] || mkdir -p "$build_dir"

do_download  "$src_url"   "$ttl_file"
do_convert   "$ttl_file"  "$rdf_file"
do_generate  "$rdf_file"  "$gen_file"
do_update    "$gen_dir"   "$dst_dir"
